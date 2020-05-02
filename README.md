# subscrbeurltool

自定义订阅 

mkdir subscrbeurltool

cd  subscrbeurltool

git pull https://github.com/available2099/subscrbeurltool.git

docker build . -t subscrbetool

docker run -d -p 8085:8888  --name subscrbetool subscrbetool
