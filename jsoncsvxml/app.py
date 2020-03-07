#encoding:utf-8

from handle_files.json_2csv import HandleCsv
from modules.movies import Movie
from handle_files.csv_2xml import CvsToXml

if __name__ == '__main__':
    # handlemovie = Movie()
    # #handle_csv = HandleCsv(filename='dict2movies.csv')
    # handle_csv1 = HandleCsv()
    # # movies = []
    # # for n in range(11):
    # #     html = handlemovie.parse_url(n)
    # #     movie = handlemovie.get_movies(html)
    # #     movies.append(movie)
    #
    # #handle_csv.write_csv_dict(movies)
    # #handle_csv1.write_csv(movies)
    # handle_csv1.read_csv()
    csvToXml = CvsToXml(csv_file_name='movies.csv')
    csvToXml.csv_to_xml(out_xml_file='movies.xml')
