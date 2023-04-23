	--SELECT --> secme, gosterme

--SELECT 5
--SELECT 5 AS 'toplam'
--SELECT 4+5+45 AS toplam
--SELECT 'bu bir deneme sorgu' AS sonuc
--select 4*7 as carpim
--SELECT 4 * 'merhaba' AS sonuc  -- hata verir

-- String birleþtirme
SELECT 'merhaba' + ' günaydýn' AS selam
SELECT 'merhaba PAÜ YBS VTY dersi öðrencileri' AS sonuc

-- Textin belirli bir kýsmýný alma
-- ilk parametre nereden baþlayacaðýný
-- ikinci parametre kaç adým ilerleyeceðini belirtir
SELECT SUBSTRING('merhaba PAÜ YBS VTY dersi öðrencileri',0,8) AS parcalanmýs

-- Bir stringin solundan 6 karakteri alýr
SELECT LEFT('bu bir denemedir', 6) AS soldan

-- Bir stringin saðýndan 6 karakter alýr
SELECT RIGHT('bu bir denemedir', 6) AS sagdan

-- stringi büyük harfe cevirme
SELECT UPPER('bu kucuk harfle yazýlmýs bir text') AS buyuk

-- stringi kücük harfe cevirme
SELECT LOWER('BU BUYUK HARFLE YAZILMIS BIR TEXT') AS kucuk

-- string uzunlugu
SELECT LEN('merhaba dunya') AS sayi

-- string içindeki bir kýsmý deðiþtirme
SELECT REPLACE('merhaba dunya','merhaba','selam') AS replace

-- string ifadenin tersi
SELECT REVERSE('merhaba dunya') AS reverse

-- string soldan bosluk silme
SELECT LTRIM('              merhaba dünya') AS soldanbosluk

-- string sagdan bosluk silme
SELECT RTRIM('merhaba dünya        ') AS soldanbosluk

-- string iki taraftan da bosluk silme
SELECT RTRIM(LTRIM('        test        '))

-- pi sayisi
SELECT PI() AS pi
SELECT PI() * 10 * 10 AS alan

-- power metodu, üssü
SELECT PI() * POWER(10,2) AS alan
SELECT POWER(5,3) AS kup

-- mutlak deger
SELECT ABS(-123213) AS mutlak

-- tarih
SELECT GETDATE() AS tarih
SELECT YEAR(GETDATE()) AS yil
SELECT MONTH(GETDATE()) AS ay
SELECT DAY(GETDATE()) AS gun

SELECT 'It''s a pencil' 

SELECT CAST(DAY('2023.03.30') AS CHAR(2)) + '.gundeyiz'
SELECT YEAR('2023.03.30') * 2 -- 60

SELECT SIN(60) AS sinus
SELECT COS(60) AS cosinus
SELECT TAN(60) AS tangent

-- tablo gorunumu
SELECT 40 AS derece, SIN(40) AS sinus, COS(40) AS cosinus, TAN(40) AS tangent
SELECT 'merhaba', 'naber', 'nasýlsýn', 'iyi misin'

-- kök alma
SELECT SQRT(64) AS kok

--kare alma
SELECT SQUARE(5) AS kare

-- yukarý yuvarlama
SELECT CEILING(12.7778) AS yukari

-- asagý yuvarla
SELECT FLOOR(12.7778) AS asagi

-- rount
SELECT ROUND(12.26326, 4) AS yuvarla

