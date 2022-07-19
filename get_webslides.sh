curl -L -o webslides.zip https://github.com/webslides/WebSlides/releases/download/1.5.0/webslides.zip
unzip webslides.zip -d webslides
DESTINATION=webslides_builder/themes/webslides_base/static
mkdir $DESTINATION
mkdir $DESTINATION/css
mkdir $DESTINATION/js
cp -R webslides/static/css/* $DESTINATION/css
cp -R webslides/static/js/* $DESTINATION/js
rm -rf webslides
rm webslides.zip