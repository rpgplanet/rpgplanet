from fabric.api import *

# Default release is 'current'
env.release = 'current'
env.anonpassword = 'wGRhhWjpatVqaAeyYUBsUxsrUQtRyz'
env.repository = 'git://melissar.dnsalias.net/home/almad/repositories/rpgplanet'

env.settings = 'production'
env.path = '/srv/www/rpgplanet.cz/www_root/www/applications'
env.mediapath = '/srv/www/rpgplanet.cz/www_root/www/htdocs/media'
env.hosts = ['kenshin.include.cz']
env.user = 'w-rpgplanet-cz'

def setup():
    """
    Setup a fresh virtualenv and install everything we need so it's ready to
    deploy to
    """
    run('mkdir -p $(path); cd $(path); virtualenv .; mkdir releases; mkdir shared;')
    download_release()
    install_requirements()

def deploy():
    """Deploy the latest version of the site to the server and restart lighttpd"""
    run('uname -a')
#    symlink_current_release()
#    migrate()
#    restart_lighttpd()

def download_release():
    """Do initial clone of the git repo"""
    run('cd $(path); wget --nd http://anonymouse:$(anonpassword)/releases/rpgplanet.cz/')

def install_requirements():
    """Install the required packages using pip"""
    run('cd $(path); pip install -E . -r ./releases/$(release)/freezed-requirements.txt')

def symlink_current_release():
    """Symlink our current release, uploads and settings file"""
    run('cd $(path); rm project; ln -s releases/current project; rm releases/current; ln -s $(release) releases/current')
    run('cd $(path)/releases/current/; ln -s settings_$(settings).py settings.py', fail='ignore')
    run('cd $(path)/releases/current/media/; ln -s ../../../shared/uploads/ .', fail='ignore')

def migrate():
    """Run our migrations"""
    run('cd $(path)/releases/current;  ../../bin/python manage.py syncdb --noinput --migrate')

def restart_lighttpd():
    """Restart the web server"""
    sudo('/etc/init.d/lighttpd restart')

