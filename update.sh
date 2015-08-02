waitressid=`ps aux | grep waitress |  awk -F ' ' '{print $2; exit;}'`
kill $waitressid

cd `pwd`
git pull

source conf/defaults.env
./biostar.sh waitress

