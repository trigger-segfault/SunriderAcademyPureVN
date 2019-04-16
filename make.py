import datetime
import os
import shutil
import subprocess
import sys
import argparse

# Definitions
prog = 'make.py'
default_out = 'deploydir.txt'

prefix = 'purevn'
srcdir = 'src'
resdir = 'resources'
outdir = 'build'
gamedir = 'game'
modsdir = 'mods'
modname = prefix
rpaprefix = 'mods/purevn/'
ignore_char = '>'
exts = ['.rpy','.rpyc','.py']
rpy_insert_first = ['class','start']

rpas = []
modules = []

def print_section(name):
    print('====== {0} ======'.format(name))
def print_status(action, name = None):
    if (name is None):
        print('{0}:'.format(action))
    else:
        print('{0}: {1}'.format(action, name))
def print_item(action, name):
    print('{0:>10} -> {1}'.format(action, name))

def renpy_make_clean_file(dstpath):
    if os.path.isfile(dstpath):
        os.remove(dstpath)
        print_item('Cleaned', dstpath)

def renpy_make_deploy_file(srcpath, relpath, deploydir, basename=False):
    if relpath is None:
        relpath = os.path.basename(srcpath)
    dstpath = os.path.join(deploydir, relpath)
    parentdir = os.path.abspath(os.path.join(dstpath, os.pardir))
    if not os.path.isdir(parentdir):
        os.makedirs(parentdir)
    if not os.path.isfile(dstpath):
        shutil.copy(srcpath, dstpath)
        print_item('Deployed', dstpath)
    else:
        print_item('Exists', dstpath)

def renpy_make_clean_files(deploydir, args):
    # Only cleanup files starting with the prefix
    clean_files = [f for f in os.listdir(deploydir) if f.startswith(prefix)]

    for srcname in clean_files:
        dstpath = os.path.join(deploydir, srcname)
        renpy_make_clean_file(dstpath)
        if dstpath.endswith('.rpy'):
            renpy_make_clean_file(dstpath + 'c') # Compiled script

def renpy_make_deploy_files(deploydirgame, deploydirmod, args):
    # Deploy Ren'Py scripts
    for module in modules:
        if not module.is_valid:
            continue
        if args.debug == False:
            renpy_make_deploy_file(module.build_file, None, deploydirmod)
        else:
            for srcpath, relpath in zip(module.source_files, module.relative_files):
                renpy_make_deploy_file(srcpath, relpath, deploydirmod)

    # Deploy Ren'Py archives
    for rpa in rpas:
        if not rpa.is_valid:
            continue
        if not rpa.is_root:
            renpy_make_deploy_file(rpa.build_file, None, deploydirgame)
        else:
            for respath, relpath in zip(rpa.resource_files, rpa.files):
                renpy_make_deploy_file(respath, relpath, deploydirmod)
                # outf = os.path.join(deploydirmod, f)
                # renpy_make_deploy_file()
                # parentdir = os.path.abspath(os.path.join(outf, os.pardir))
                # if os.path.isdir(parentdir):
                #     os.makedirs(parentdir)
                # shutil.copy(f, outf)
            #renpy_make_deploy_file(rpa.build_file, deploydirmod)

def renpy_make_deploy(args):
    if args.clean == True:
        print_section('Cleaning')
    else:
        print_section('Deploying')

    with open(args.out) as deployfile:
        for deploydir in deployfile:
            # Strip newlines
            deploydir = deploydir.rstrip()
            if deploydir == '' or deploydir.startswith(ignore_char):
                continue
            # Get mods and mod subdirectory
            deploydirgame = os.path.join(deploydir, gamedir)
            deploydirmods = os.path.join(deploydirgame, modsdir)
            deploydirmod = os.path.join(deploydirmods, modname)
            #deploydirmod = os.path.join(deploydirmods, modname)

            if not os.path.isdir(deploydirmods):
                os.mkdir(deploydirmods)
            if not os.path.isdir(deploydirmod):
                os.mkdir(deploydirmod)

            if args.clean == True:
                print_status('Cleaning in', deploydirmod)
            else:
                print_status('Deploying to', deploydirmod)

            #renpy_make_clean_files(deploydirmod, args)
            shutil.rmtree(deploydirmod)
            if args.deploy == True or args.debug == True:
                renpy_make_deploy_files(deploydirgame, deploydirmod, args)
            print()

def renpy_make_compile(args):
    print_section('Compiling')
    for module in modules:
        if not module.is_valid:
            continue
        module.compile()

def renpy_make_archive(args):
    print_section('Archiving')
    for rpa in rpas:
        if not rpa.is_valid or not rpa.is_root:
            continue
        rpa.archive()

def renpy_make_run(args):
    global modules
    global rpas

    if not os.path.isdir(outdir):
        os.makedirs(outdir)

    modules = [RenPyMakeModule()]
    modules += ([
        RenPyMakeModule(d) for d in os.listdir(srcdir)
        if os.path.isdir(os.path.join(srcdir, d))
    ])

    rpas = [RenPyMakeRpa()]
    rpas += ([
        RenPyMakeRpa(f) for f in os.listdir(resdir)
        if os.path.isfile(os.path.join(resdir, f)) and f.endswith('.rpa') and not f.startswith(prefix)
    ])

    # Cleanup build scripts
    for fname in os.listdir(outdir):
        fpath = os.path.join(outdir, fname)
        if os.path.isfile(fpath) and (fpath.endswith('.rpy') or fpath.endswith('.py')):
            os.remove(fpath)

    # Compile build scripts
    if args.build == True or args.deploy == True:
        renpy_make_compile(args)

    # Archive build resources
    #if args.build == True or args.deploy == True or args.debug == True:
    #    renpy_make_archive(args)

    # Deploy build files to output directories
    if args.deploy == True or args.debug == True or args.clean == True:
        renpy_make_deploy(args)
            
    # Finished timestamp
    print_status('Finished', datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))

class RenPyMakeRpa(object):
    def __init__(self, existing_file = None):
        self.files = []
        self.name = prefix
        self.is_existing = False
        if existing_file is None:
            self.traverse_files()
        else:
            self.name = os.path.splitext(existing_file)[0]
            self.is_existing = True
    
    def traverse_files(self, relpath = '.'):
        path = os.path.join(resdir, relpath)
        if relpath == '.':
            path = resdir
        for fname in os.listdir(path):
            fpath = os.path.join(path, fname)
            frelpath = os.path.join(relpath, fname)
            if relpath == '.':
                frelpath = fname

            if os.path.isfile(fpath) and (fname.endswith('.png') or fname.endswith('.jpg')):
                self.files.append(frelpath)
            elif os.path.isdir(fpath):
                self.traverse_files(frelpath)

    @property
    def is_root(self):
        return self.name == prefix
    
    @property
    def resource_files(self):
        return [os.path.join(resdir, f) for f in self.files]

    @property
    def build_file(self):
        return os.path.join(resdir, '{0}.rpa'.format(self.name))

    @property
    def is_valid(self):
        return len(self.files) != 0 or self.is_existing

    def archive(self):
        if os.path.isfile(self.build_file):
            os.remove(self.build_file)

        print_status('Archiving', self.build_file)
        rpaargs = ([
            sys.executable,
            '../rpatool',
            '-c',
            os.path.join('..', self.build_file)
        ]) + ['{0}{1}={1}'.format(rpaprefix, f) for f in self.files]

        # Temporarily change the working directory
        cwd = os.getcwd()
        for frelpath in self.files:
            print_item('Packing', frelpath)
        os.chdir(resdir)
        subprocess.Popen(rpaargs, shell=True).wait()
        os.chdir(cwd)

        if not os.path.isfile(self.build_file):
            print_status('Archiving of file failed', self.name)
            sys.exit()

        print_item('Archived', self.build_file)
        print()

class RenPyMakeModule(object):
    def __init__(self, directory = None):
        self.files = []
        self.name = prefix
        self.path = ''
        if not directory is None:
            self.name = '{0}_{1}'.format(prefix, directory)
            #self.path = os.path.join(srcdir, directory)
            self.path = directory
        self.files = os.listdir(self.source_path)
        self.files = [f for f in self.files if os.path.isfile(os.path.join(self.source_path, f))]

        self.files = [f for f in self.files if f.startswith(self.name)]

        self.insert_first(*rpy_insert_first)

    def insert_first(self, *args):
        postfixes = reversed(args)
        for postfix in postfixes:
            fname = '{0}_{1}.rpy'.format(self.name, postfix)
            insertfiles = [f for f in self.files if f == fname]
            if len(insertfiles) == 1:
                self.files.remove(insertfiles[0])
                self.files.insert(0, insertfiles[0])

    @property
    def is_root(self):
        return self.path == ''

    @property
    def source_path(self):
        if self.is_root:
            return srcdir
        return os.path.join(srcdir, self.path)
    
    @property
    def source_files(self):
        return [os.path.join(self.source_path, f) for f in self.files]

    @property
    def relative_files(self):
        if self.is_root:
            return self.files
        return [os.path.join(self.path, f) for f in self.files]

    @property
    def build_file(self):
        return os.path.join(outdir, '{0}.rpy'.format(self.name))

    @property
    def is_valid(self):
        return len(self.files) != 0

    def compile(self):
        print_status('Compiling to', self.build_file)

        # Remove the original file
        if os.path.isfile(self.build_file):
            os.remove(self.build_file)

        # Append all files to a single output file
        with open(self.build_file, 'w') as outfile:
            for srcrelpath in self.relative_files:

                outfile.write('#########################################\n')
                outfile.write('# file: {0}\n\n'.format(srcrelpath))

                srcpath = os.path.join(srcdir, srcrelpath)
                endswith_newline = False
                with open(srcpath) as infile:
                    for line in infile:
                        outfile.write(line)
                        endswith_newline = line.endswith('\n') or line.endswith('\r')
                
                outfile.write('\n')
                if endswith_newline == False:
                    outfile.write('\n')
                print_item('Appended', srcrelpath)
        print_item('Compiled', self.build_file)
        print()

def main(argv):
    parser = argparse.ArgumentParser(
        prog=prog,
        usage='python make.py [-b|-d|-dbg|-c] [-o [OUT=\'{0}\']]'.format(default_out),
        description='A python script for comiling Ren\'Py mods.',
        epilog='You may only pass up to one [-b|-d|-dbg|-c|-h] switch to {0}. In the \'OUT\' deployment file, lines starting with \'{1}\' are ignored.'.format(prog, ignore_char),
        add_help=False)

    parser.add_argument('-b', '--build', action='store_true', help='Build modules and rpas.')
    parser.add_argument('-d', '--deploy', action='store_true', help='Build and deploy modules and rpas.')
    parser.add_argument('-dbg', '--debug', action='store_true', help='Deploy source files and rpas.')
    parser.add_argument('-c', '--clean', action='store_true', help='Cleanup all deployed files (except large rpas).')
    parser.add_argument('-o', '--out', nargs=1, default=default_out, help='Specify the file listing directories to deploy to.')

    parser.add_argument('-h', '--help', action='store_true', help='Print this help and exit.')
    args = parser.parse_args(argv)

    switch_count = 0
    for arg in args.__dict__:
        arg = args.__dict__[arg]
        if type(arg) == bool and arg == True:
            switch_count += 1
    if switch_count > 1:
        print('{0}: error: Too many action switches (-b|-d|-dbg|-c|-h) passed: {1}'.format(parser.prog, switch_count))
        return

    if switch_count == 0 or args.help == True:
        parser.print_help()
        return

    if isinstance(args.out, list):
        args.out = args.out[0]
    renpy_make_run(args)

if __name__ == "__main__":
    argv = sys.argv.copy()
    argv.pop(0)
    main(argv)