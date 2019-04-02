import datetime
import os
import shutil
import subprocess
import sys

def has_arg(arg):
    return (len(sys.argv) == 2 and sys.argv[1] == arg)

# Arguments
deploy = has_arg('-d') or has_arg('-dbg')
deploydbg = has_arg('-dbg')
clean = has_arg('-c')

# Definitions
initfile = 'purevn_init.rpy'
srcdir = 'src'
resdir = 'resources'
outdir = 'build'
outname = 'purevn.rpy'
outrpa = 'purevn.rpa'
outpath = os.path.join('build', outname)
outrpapath = os.path.join('build', outrpa)
deployname = 'deploydir.txt'
definefiles = False


if definefiles == True:
    # Define append order manually
    filenames = ([
        'init',
        'start',
        'debug',
        'decision',
        'maps',
        'choose_outcome',
        'choose_lunch',
        'choose_club',
        'choose_afterschool',
        'activities'
    ])
    rpafiles = ([
        'UI/purevn_go_home_base.png',
        'UI/purevn_go_home_hover.png'
    ])
    # Give the full file names
    filenames = ['purevn_{0}.rpy'.format(f) for f in filenames]
else:
    # Just get the filenames and append them in loaded order
    filenames = os.listdir(srcdir)
    rpafiles = os.listdir(os.path.join(resdir, 'UI'))
    # Ignore directories
    filenames = [f for f in filenames if os.path.isfile(os.path.join(srcdir, f))]
    # Make sure this is a purevn source file
    filenames = [f for f in filenames if f.startswith('purevn_') and f.endswith('.rpy')]
    # Prepend UI/ folder
    rpafiles = [os.path.join('UI', f) for f in rpafiles]


# Insert init file first for clarity
filenames = [f for f in filenames if f != initfile]
filenames.insert(0, initfile)

if clean == True:
    if os.path.isfile(outpath):
        os.remove(outpath)
        print(' Cleaned -> {0}'.format(outpath))
        
elif deploydbg == False:
    # Make sure the output directory exists
    if not os.path.isdir(outdir):
        os.mkdir(outdir)

    if os.path.isfile(outpath):
        os.remove(outpath)

    print('Compiling to: {0}'.format(outpath))

    # Append all files to a single output file
    with open(outpath, 'w') as outfile:
        for fname in filenames:

            outfile.write('#########################################\n')
            outfile.write('# file: {0}\n'.format(fname))
            outfile.write('\n')

            fpath = os.path.join(srcdir, fname)
            with open(fpath) as infile:
                for line in infile:
                    outfile.write(line)
            outfile.write('\n')
            print('Appended -> {0}'.format(fname))
    print('Compiled -> {0}'.format(outpath))

# Build rpa archive
if deploy == True:
    if os.path.isfile(outrpapath):
        os.remove(outrpapath)

    print()
    print('Archiving:')
    #parentrpa = os.path.join('..', outrpapath)
    #rpafileargs = ' '.join('"{0}"'.format(rpafiles))
    rpaargs = ([
        sys.executable,
        '../rpatool',
        '-c',
        os.path.join('..', outrpapath)
    ]) + rpafiles
    cwd = os.getcwd()
    os.chdir(resdir)
    subprocess.Popen(rpaargs, shell=True).wait()
    os.chdir(cwd)

    if not os.path.isfile(outrpapath):
        print('Archive failed to build!');
        sys.exit()

    print('Archived -> {0}'.format(outrpa))

# Optional deploy for testing
if (clean == True or deploy == True) and not os.path.isfile(deployname):
    print('Error: There is no "{0}" file to determine deploy location!'.format(deployname))
elif (clean == True or deploy == True):
    with open(deployname) as deployfile:
        for deploydir in deployfile:
            # Strip newlines
            deploydir = deploydir.rstrip()
            if deploydir == '':
                continue
            # Move deploydir to game/
            deploydir = os.path.join(deploydir, 'game')
            # Get deploy rpa path
            deployrpa = os.path.join(deploydir, outrpa)

            print()
            print('Deploying to: {0}'.format(deploydir))

            # Cleanup old files
            if os.path.isfile(deployrpa):
                os.remove(deployrpa)
                print(' Cleaned -> {0}'.format(deployrpa))
            cleanup_files = [f for f in os.listdir(deploydir) if f.startswith('purevn')]

            for fname in cleanup_files:
                deploypath = os.path.join(deploydir, fname)
                deploypath_c = deploypath + 'c'
                if os.path.isfile(deploypath_c):
                    os.remove(deploypath_c)
                    print(' Cleaned -> {0}'.format(deploypath_c))
                if os.path.isfile(deploypath):
                    os.remove(deploypath)
                    print(' Cleaned -> {0}'.format(deploypath))

            # Deploy new files
            if deploy == True:
                shutil.copy(outrpapath, deployrpa)
                print('Deployed -> {0}'.format(deployrpa))

                if deploydbg == False:
                    deploy_files = [ outpath ]
                else:
                    deploy_files = [os.path.join(srcdir, f) for f in filenames]
                
                for fpath in deploy_files:
                    deploypath = os.path.join(deploydir, os.path.basename(fpath))
                    shutil.copy(fpath, deploypath)
                    print('Deployed -> {0}'.format(deploypath))

# Finished timestamp
print()
print('Finished: {0}'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
