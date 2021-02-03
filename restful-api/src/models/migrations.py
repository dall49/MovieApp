
tables = [
    {
        'name' : 'categories',
        'schema' : '''
                    id int primary key auto_increment,
                    name varchar(100) unique
                   '''
    },
    {
        'name' : 'movies',
        'schema' : '''
                    id int primary key auto_increment,
                    title varchar(100) unique,
                    image varchar(100) default 'default.jpg',
                    rating float,
                    category_id int,
                    foreign key (category_id) references categories(id)
                   '''
    }
]

