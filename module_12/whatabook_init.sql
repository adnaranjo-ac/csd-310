
DROP USER IF EXISTS 'whatabook_user'@'localhost';

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);



INSERT INTO store(locale)
    VALUES('2323 Street Rd, Cityville, TX, 12345');



INSERT INTO book(book_name, author, details)
    VALUES('The Night and its Moon', 'Piper CJ', 'A book about orphans and stuff.');

INSERT INTO book(book_name, author, details)
    VALUES('Its Starts With Us: A Novel', "Colleen Hoover", "A book from Atlas perspective.");

INSERT INTO book(book_name, author, details)
    VALUES('The Midnight Library', 'Matt Haig', "In The Midnight Library, Matt Haigs enchanting blockbuster novel, Nora Seed finds herself faced with this decision. Faced with the possibility of changing her life for a new one, following a different career, undoing old breakups, realizing her dreams of becoming a glaciologist; she must search within herself as she travels through the Midnight Library to decide what is truly fulfilling in life, and what makes it worth living in the first place.");

INSERT INTO book(book_name, author, details)
    VALUES('Black Cake', 'Charmaine Wilkerson', 'Charmaine Wilkersons debut novel is a story of how the inheritance of betrayals, secrets, memories, and even names, can shape relationships and history. Deeply evocative and beautifully written, Black Cake is an extraordinary journey through the life of a family changed forever by the choices of its matriarch.' );

INSERT INTO book(book_name, author, details)
    VALUES('The Maid', 'Nita Prose', 'A Clue-like, locked-room mystery and a heartwarming journey of the spirit, The Maid explores what it means to be the same as everyone else and yet entirely different, and reveals that all mysteries can be solved through connection to the human heart.');

INSERT INTO book(book_name, author, details)
    VALUES("The Last Thing He Told Me", 'Laura Dave', 'With its breakneck pacing, dizzying plot twists, and evocative family drama, The Last THing He Told Me is a riverting mystery, certain to shock you with its final, heartbreaking turn.');

INSERT INTO book(book_name, author, details)
    VALUES('Wish You Were Here', 'Jodi Picoult', 'In the Galapagos Islands, where Darwins theory of evolution by natural selection was formed, Diana finds herself examining her relationships, her choices, and herself-and wondering if when she goes home, she too will ahve evolved into someone completely different.');

INSERT INTO book(book_name, author, details)
    VALUES('Devil House: A Novel', 'John Darnielle', 'Devil House is John Darnielles most ambitious work yet, a book that blurs the line between fact and fiction, that combines daring formal experimentation with a spellbinding tale of crime, writing, memory, and artistic obsession.');

INSERT INTO book(book_name, author, details)
    VALUES('The Song of Achilles', 'Collen McCullough', 'A thrilling, profoundly moving, and utterly unique retelling of the legend of Achilles and the Trojan War from the bestselling author of Circe.');




INSERT INTO user(first_name, last_name) 
    VALUES('Bruce', 'Wayne');

INSERT INTO user(first_name, last_name)
    VALUES('Harleen', 'Quinzel');

INSERT INTO user(first_name, last_name)
    VALUES('Pamela', 'Isley');



INSERT INTO wishlist(user_id, book_id) 
	VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Bruce'), 
        (SELECT book_id FROM book WHERE book_name = 'The Song of Achilles')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Harleen'),
        (SELECT book_id FROM book WHERE book_name = 'Devil House: A Novel')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Pamela'),
        (SELECT book_id FROM book WHERE book_name = 'Black Cake')
    );