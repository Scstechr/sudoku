import sys
import os

def main():
    path = sys.argv[1]
    filename = '{}/{}'.format(sys.argv[1],sys.argv[2])
    os.chdir(path)
    userlist = []
    with open(filename, 'r') as f:
        for line in f:
            string = line.split()
            print(string)

    #     for line in f:
    #         user = {}
    #         userid = line[:line.find(',')]
    #         username = line[line.find(',')+1:].replace('\n','')
    #         name = '{},{}'.format(userid,username)
    #         user['id'] = userid;
    #         user['name'] = username;
    #         userlist.append(user)
    #         user['size'] = 0;
    #         user['filenum'] = 0;
    #         # print(line)
    #
    # for line in userlist:
    #     print(line)
    #
    # with open('files_list.txt', 'r') as f:
    #     for line in f:
    #         if line.find('U') != 0:
    #             userid = line[line.find('U'):]
    #             userid = userid[:userid.find(',')]
    #             size = line[line.find('U'):]
    #             size = size[size.find(',')+1:]
    #             size = size[size.find(',')+1:]
    #             size = size[:size.find(',')]
    #             for user in userlist:
    #                 if user['id'] == userid:
    #                     user['size'] += int(size)
    #                     user['filenum'] += 1
    #                     break
    #
    # print("\n")
    #
    # totalsize = 0
    # for line in userlist:
    #     size = line['size']
    #     totalsize += int(size)
    #     print(totalsize)
    #
    # for line in userlist:
    #     size = line['size']
    #     line['size'] /= totalsize
    #
    # for line in userlist:
    #     print(line)
    #
    # print(len('r.takahashi'))
if __name__ == '__main__':
    main()