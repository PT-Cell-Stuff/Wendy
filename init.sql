CREATE TABLE IF NOT EXISTS channels(
    pk INTEGER PRIMARY KEY,
    name  TEXT UNIQUE,
    id INTEGER UNIQUE 
);


CREATE TABLE encryptions(

    pk INTEGER PRIMARY KEY,
    hint TEXT DEFAULT "Standard Encryption Key",
    time_generated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    nonce BLOB NOT NULL,
    jpic BLOB NOT NULL
);

CREATE TABLE IF NOT EXISTS directories(

    pk INTEGER PRIMARY KEY,
    name TEXT,
    parent_pk INTEGER, 
    is_link BOOL DEFAULT FALSE,
    target_pk INTEGER DEFAULT NULL,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    channel INTEGER NOT NULL,

    FOREIGN KEY(parent_pk) REFERENCES directories(pk) ON DELETE CASCADE,
    FOREIGN KEY(channel) REFERENCES channels(pk) ON DELETE CASCADE ON UPDATE CASCADE,        -- Individual Folders are stored in channels
    FOREIGN KEY(target_pk) REFERENCES directories(pk) ON DELETE CASCADE ON UPDATE CASCADE   -- Links are stored in directories
);


CREATE TABLE IF NOT EXISTS files(

    pk INTEGER PRIMARY KEY,
    name TEXT,
    dir_pk INTEGER,
    is_link BOOL DEFAULT FALSE,
    target_pk DEFAULT NULL,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    no_of_chunks INTEGER DEFAULT 1,
    chunks_info TEXT DEFAULT "[]",
    size INTEGER NOT NULL,
    chunk_break_size INTEGER DEFAULT 2000*1024*1024    


    FOREIGN KEY(dir_pk) REFERENCES directories(pk) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(target_pk) REFERENCES files(pk) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS backups(

    pk INTEGER PRIMARY KEY,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    name TEXT UNIQUE,
    filepath TEXT DEFAULT NULL, 
    file_pk INTEGER DEFAULT NULL,

    FOREIGN KEY(file_pk) REFERENCES files(pk)
    CHECK (filepath is not NULL or file_pk is not NULL)

);

