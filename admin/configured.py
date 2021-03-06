from os.path import join

PREFIX          = "/usr/local/zenloadbalancer/app/cherokee"
LIBDIR          = "/usr/local/zenloadbalancer/app/cherokee/lib"
DATADIR         = "/usr/local/zenloadbalancer/app/cherokee/share"
DOCDIR          = "/usr/local/zenloadbalancer/app/cherokee/share/doc/cherokee"
LOCALEDIR       = "/usr/local/zenloadbalancer/app/cherokee/share/locale"
WWWROOT         = "/usr/local/zenloadbalancer/www"
SYSCONFDIR      = "/usr/local/zenloadbalancer/app/cherokee/etc"
LOCALSTATE      = "/usr/local/zenloadbalancer/app/cherokee/var"
VERSION         = "1.2.104"

CHEROKEE_SERVER       = join (PREFIX, "sbin/cherokee")
CHEROKEE_WORKER       = join (PREFIX, "sbin/cherokee-worker")
CHEROKEE_ADMINDIR     = join (PREFIX, "share/cherokee/admin")
CHEROKEE_ICONSDIR     = join (PREFIX, "share/cherokee/icons")
CHEROKEE_THEMEDIR     = join (PREFIX, "share/cherokee/themes")
CHEROKEE_PANIC_PATH   = join (PREFIX, "bin/cherokee-panic")
CHEROKEE_PLUGINDIR    = join (LIBDIR, "cherokee")
CHEROKEE_DATADIR      = join (DATADIR, "cherokee")
CHEROKEE_DEPSDIR      = join (DATADIR, "cherokee/deps")
CHEROKEE_CONFDIR      = join (SYSCONFDIR, "cherokee")
CHEROKEE_VAR_LOG      = join (LOCALSTATE, "log")
CHEROKEE_VAR_RUN      = join (LOCALSTATE, "run")
CHEROKEE_VAR_LIB      = join (LOCALSTATE, "lib/cherokee")
CHEROKEE_RRD_DIR      = join (LOCALSTATE, "lib/cherokee/graphs")
