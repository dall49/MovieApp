

tables = [
    {
        'name' : 'categories',
        'schema' : '''
                    id integer primary key autoincrement,
                    name varchar(100) unique
                   '''
    },
    {
        'name' : 'movies',
        'schema' : '''
                    id integer primary key autoincrement,
                    title varchar(100) unique,
                    image varchar(100) default 'default.jpg',
                    rating float,
                    category_id integer,
                    foreign key (category_id) references categories(id)
                   '''
    }
]

