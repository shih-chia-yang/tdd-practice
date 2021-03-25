 synchronizing two file directories

1. if a file exists in the source but not in the destination , copy the file over

2. if file exists in the source , but it has a different name than in the destination, rename the destination file to match

3. if a file exist in the destination but not in the source ,remove it 


- walk the source folder and build a dict of filenames and their hashes
    - [x] get target folder total files count
    - [x] use dict save all files and file hash
    - [x] move file, copy file ,delete file
    - [x] abstract function