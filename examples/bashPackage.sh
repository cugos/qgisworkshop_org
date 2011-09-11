#! /bin/bash
logfile=$(dirname $0)/output.log
for FILE in $(find * -type d);
do
    BEGTIMESTAMP_PDT=$(date)
    echo "\nSTART: " $FILE " at >>> " $BEGTIMESTAMP_PDT "\n" >> $logfile 2>&1
    cd $FILE
    rm resources.py
    rm ui*.py
    make >> $logfile 2>&1
    cd ..
    zip -9vr $FILE.zip $FILE/* >> $logfile 2>&1
    ENDTIMESTAMP_PDT=$(date)
    echo "\nEND: " $FILE " at >>> " $ENDTIMESTAMP_PDT "\n" >> $logfile 2>&1
done;

exit 0

