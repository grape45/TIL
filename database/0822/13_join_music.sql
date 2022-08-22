SELECT * FROM album JOIN artists ON albums.ArtistID = artists.ArtistID LIMIT 5;

SELECT * FROM album LEFT JOIN artists ON albums.ArtistId = artists.ArtistId LIMIT 5;