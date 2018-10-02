'''
to split file into small part for pilot study
'''
import sys
import os


def splitfile(file_path, line_size=1000000):
    file_dir, name = os.path.split(file_path)
    name, ext = os.path.splitext(name)
    file_dir = os.path.join(file_dir, name)
    if not os.path.exists(file_dir):
        os.mkdir(file_dir)


    stream = open(file_path, 'r', encoding = 'utf-8')

    part_file_name = os.path.join(file_dir, name + '_' + 'test' + ext)
    print('write start %s' % part_file_name)
    part_stream = open(part_file_name, 'w', encoding='utf-8')

    read_count = 0
    while read_count < line_size:
        read_content = stream.readline()
        if read_content:
            part_stream.write(read_content)
        else:
            break
        read_count += 1

    part_stream.close()
    print('done')


if __name__ == '__main__':
    # splitfile(sys.argv[1], sys.argv[2])
    splitfile(r'C:/Users/Student/Desktop/Acquire Valued Shoppers Challenge/data/sampleSubmission.csv', 6000)