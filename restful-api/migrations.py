

tables = [
    {
        'name' : 'categories',
        'schema' : '''
                    id integer primary key autoincrement,
                    name varchar(100)
                   '''
    },
    {
        'name' : 'movies',
        'schema' : '''
                    id integer primary key autoincrement,
                    title varchar(100),
                    image varchar(100),
                    rating float,
                    category_id integer,
                    foreign key (category_id) references categories(id)
                   '''
    }
]

