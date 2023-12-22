from database.db import get_connection
from .entities.Movie import Movie

class MovieModel():
    
    
    @classmethod
    def get_movies(self):
        try:
            # una coenxion que sea = a la exec de la function get_connection
            connection = get_connection()
            movies = []
            
            with connection.cursor() as cursor:
                cursor.execute("select id, title, duration, released from movie order by title asc")  
                resultset = cursor.fetchall()
                
                for row in resultset:
                    movie = Movie(row[0], row[1], row[2], row[3])
                    # error -->  "message": "Object of type Movie is not JSON serializable" anexamos to_JSON
                    movies.append(movie.to_JSON())       
                    
            connection.close()
            return movies    
        except Exception as ex:
            raise Exception(ex)
        
        
    @classmethod
    def get_movie(self, id):
        try:
            # una coenxion que sea = a la exec de la function get_connection
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("select id, title, duration, released from movie where id = %s", (id,))  
                row = cursor.fetchone()
                
                movie = None
                if row != None:
                    movie = Movie(row[0], row[1], row[2], row[3])
                    # error -->  "message": "Object of type Movie is not JSON serializable" anexamos to_JSON
                    movie = movie.to_JSON()     
                    
            connection.close()
            return movie
        except Exception as ex:
            raise Exception(ex)
        
        
    @classmethod
    def add_movie(self, movie):
        try:
            # una coenxion que sea = a la exec de la function get_connection
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("""insert into movie (id, title, duration, released)
                        values (%s, %s, %s, %s)""", (movie.id, movie.title, movie.duration, movie.released))
            affected_rows = cursor.rowcount
            connection.commit()         
                     
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
        

    @classmethod
    def update_movie(self, movie):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("""update movie set title = %s, duration = %s, released = %s
                        where id = %s""", (movie.title, movie.duration, movie.released, movie.id))
            affected_rows = cursor.rowcount
            connection.commit()         
                     
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)



    @classmethod
    def delete_movie(self, movie):
        try:
            # una coenxion que sea = a la exec de la function get_connection
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("delete from movie where id = %s", (movie.id, ))
                affected_rows = cursor.rowcount
                connection.commit()         
                        
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
        
