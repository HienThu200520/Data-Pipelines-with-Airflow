-- Create the artists table
CREATE TABLE IF NOT EXISTS public.artists (
    artistid VARCHAR(256) NOT NULL,
    name VARCHAR(256),
    location VARCHAR(256),
    latitude NUMERIC(18,0),
    longitude NUMERIC(18,0),
    PRIMARY KEY (artistid)
);

-- Create the songplays table
CREATE TABLE IF NOT EXISTS public.songplays (
    playid VARCHAR(32) NOT NULL,
    start_time TIMESTAMP NOT NULL,
    userid INT NOT NULL,
    "level" VARCHAR(256),
    songid VARCHAR(256),
    artistid VARCHAR(256),
    sessionid INT,
    location VARCHAR(256),
    user_agent VARCHAR(256),
    PRIMARY KEY (playid)
);

-- Create the songs table
CREATE TABLE IF NOT EXISTS public.songs (
    songid VARCHAR(256) NOT NULL,
    title VARCHAR(256),
    artistid VARCHAR(256),
    year INT,
    duration NUMERIC(18,0),
    PRIMARY KEY (songid)
);

-- Create the staging_events table
CREATE TABLE IF NOT EXISTS public.staging_events (
    artist VARCHAR(256),
    auth VARCHAR(256),
    firstname VARCHAR(256),
    gender VARCHAR(256),
    iteminsession INT,
    lastname VARCHAR(256),
    length NUMERIC(18,0),
    "level" VARCHAR(256),
    location VARCHAR(256),
    method VARCHAR(256),
    page VARCHAR(256),
    registration NUMERIC(18,0),
    sessionid INT,
    song VARCHAR(256),
    status INT,
    ts BIGINT,
    useragent VARCHAR(256),
    start_time TIMESTAMP,
    userid INT
);

-- Create the staging_songs table
CREATE TABLE IF NOT EXISTS public.staging_songs (
    num_songs INT,
    artist_id VARCHAR(256),
    artist_name VARCHAR(256),
    artist_latitude NUMERIC(18,0),
    artist_longitude NUMERIC(18,0),
    artist_location VARCHAR(256),
    song_id VARCHAR(256),
    title VARCHAR(256),
    duration NUMERIC(18,0),
    year INT
);

-- Create the time table
CREATE TABLE IF NOT EXISTS public."time" (
    start_time TIMESTAMP NOT NULL,
    "hour" INT,
    "day" INT,
    week INT,
    "month" VARCHAR(256),
    "year" INT,
    weekday VARCHAR(256),
    PRIMARY KEY (start_time)
);

-- Create the users table
CREATE TABLE IF NOT EXISTS public.users (
    userid INT NOT NULL,
    first_name VARCHAR(256),
    last_name VARCHAR(256),
    gender VARCHAR(256),
    "level" VARCHAR(256),
    PRIMARY KEY (userid)
);
