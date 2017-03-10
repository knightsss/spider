#cosing=utf-8
__author__ = 'shifeixiang'
import simplejson

def get_data():

    with open('json5.txt','r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            json_line = simplejson.loads(line)
            print type(json_line)
            # print json_line

    print len(json_line['data'])
    for cloumn in json_line['data']:
        print cloumn
        print cloumn['title']
        print "----"
        # print json_line['data'][count]
        # print json_line['data'][count]['title']
        # print json_line['data'][0]['abstract']
    # print json_line['data'][1]
    # print json_line['data'][1]['title']
    # print json_line['data'][1]['abstract']
    # print json_line['data'][2]
    # print json_line['data'][2]['title']
    # print json_line['data'][3]
    # print json_line['data'][3]['title']


if __name__ == '__main__':
    get_data()