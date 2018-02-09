cd tarballs
rm *.tar.gz
cd ..
tar -cvzf rootfiles_main.tar.gz rootfiles_main
tar -cvzf logs_main_matrix.tar.gz logs_main_matrix
tar -cvzf data_main_matrix.tar.gz data_main_matrix
mv *.tar.gz tarballs/
