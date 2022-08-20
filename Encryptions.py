import jihyocrypt as jihyo  


def make_encryption(hint, password , cursor):
    
    vals = jihyo.key_maker(password , redundant = True)
    
    cursor.execute("INSERT INTO encryptions (hint, nonce , jpic) VALUES (?,?,?)" , (hint, memoryview(vals[0]) , memoryview(vals[1])))
    cursor.execute("select last_inserted_rowid();").fetchone()[0]