from typing import Dict, Any
from sqlalchemy.orm import Session
from models.models import Artwork
from sqlalchemy import desc


class ArtworkRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    def insert_artwork(self, artwork: Artwork) -> bool: 
        try:
            self.sess.add(artwork)
            self.sess.commit()
        except Exception as e:
            print(e) 
            return False 
        return True
    
    def update_artwork(self, artwork_id:int, details:Dict[str, Any]) -> bool: 
       try:
             self.sess.query(Artwork).filter(Artwork.artwork_id == artwork_id).update(details)     
             self.sess.commit() 
       except Exception as e:
             print(e) 
       return True
   
    def delete_artwork(self, artwork_id:int) -> bool: 
        try:
           art = self.sess.query(Artwork).filter(Artwork.artwork_id == artwork_id).delete()
           self.sess.commit()
          
        except Exception as e:
           print(e) 
        return True
    
    def get_all_artworks(self):

        artworks = self.sess.query(Artwork).all()
        return  artworks
    
    def get_artwork(self, artwork_id:int): 
        return self.sess.query(Artwork).filter(Artwork.artwork_id == artwork_id).one_or_none()