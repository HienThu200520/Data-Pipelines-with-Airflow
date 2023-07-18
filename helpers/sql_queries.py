class SqlQueries:
    songplay_table_insert = ("""
        INSERT INTO songplays (playid, start_time, userid, level, songid, artistid, sessionid, location, user_agent)
        SELECT
            md5(events.sessionid || events.start_time) AS playid,
            events.start_time,
            events.userid,
            events.level,
            songs.songid,
            songs.artistid,
            events.sessionid,
            events.location,
            events.useragent AS user_agent
        FROM staging_events AS events
        JOIN staging_songs AS songs ON (events.song = songs.title AND events.artist = songs.artist_name)
        WHERE events.page = 'NextSong'
    """)

    user_table_insert = ("""
        INSERT INTO users (userid, first_name, last_name, gender, level)
        SELECT DISTINCT
            userid,
            firstname,
            lastname,
            gender,
            level
        FROM staging_events
        WHERE page = 'NextSong' AND userid IS NOT NULL
    """)

    song_table_insert = ("""
        INSERT INTO songs (songid, title, artistid, year, duration)
        SELECT DISTINCT
            song_id,
            title,
            artist_id,
            year,
            duration
        FROM staging_songs
    """)

    artist_table_insert = ("""
        INSERT INTO artists (artistid, name, location, lattitude, longitude)
        SELECT DISTINCT
            artist_id,
            artist_name,
            artist_location,
            artist_latitude,
            artist_longitude
        FROM staging_songs
    """)

    time_table_insert = ("""
        INSERT INTO time (start_time, hour, day, week, month, year, weekday)
        SELECT DISTINCT
            start_time,
            EXTRACT(hour FROM start_time),
            EXTRACT(day FROM start_time),
            EXTRACT(week FROM start_time),
            EXTRACT(month FROM start_time),
            EXTRACT(year FROM start_time),
            EXTRACT(weekday FROM start_time)
        FROM songplays
    """)
