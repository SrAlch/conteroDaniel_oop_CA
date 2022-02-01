INSERT INTO patient
VALUES (1, 'Helyn', 'Grannie', 'Leggott', '7 Del Sol Alley', 'Funga', "3255346", '+62 333 135 9283', 'Grannie Leggott', '+62 211 440 9599'),
        (2, 'Glyn', 'Kennedy', 'Curnnokk', '034 Corry Parkway', 'Sakaiminato', '690-1315', '+81 548 345 5348', 'Kennedy Curnnokk', '+1 314 900 6786'),
        (3, 'Mureil', 'Augusta', 'Witchard', '42507 Ilene Avenue', 'San Juan Bautista', "4534556", '+58 277 979 6881', 'Augusta Witchard', '+63 470 340 0938'),
        (4, 'Merrielle', 'Raymond', 'Toffano', '20512 Autumn Leaf Parkway', 'Vicente Guerrero', '71122', '+52 382 964 6976', 'Raymond Toffano', '+63 305 885 1760'),
        (5, 'Ania', 'Ester', 'Wincer', '57960 Clove Pass', 'Hefu', "564356", '+86 840 500 7345', 'Ester Wincer', '+233 434 342 7482'),
        (6, 'Dulcea', 'Larissa', 'Pendrill', '0966 Monica Pass', 'Sobreira', '4640-545', '+351 893 870 2273', 'Larissa Pendrill', '+49 285 169 6017'),
        (7, 'Lorine', 'Giselle', 'Kilpin', '9984 Hansons Hill', 'Shanxia', "DO7R412", '+86 652 257 2965', 'Giselle Kilpin', '+63 760 640 3073'),
        (8, 'Nollie', 'Loreen', 'Mumm', '77636 Larry Hill', 'Qiancheng', "28760", '+86 696 279 1379', 'Loreen Mumm', '+86 143 843 2144'),
        (9, 'Parke', 'Alice', 'Presnell', '061 Vidon Terrace', 'Tatsuno', '979-1501', '+81 433 232 5987', 'Alice Presnell', '+86 435 568 9222'),
        (10, 'Leena', 'Tom', 'Braz', '40 Mallard Junction', 'Aviles', '33404', '+34 868 589 8947', 'Tom Braz', '+351 703 955 1252');

INSERT INTO doctor
VALUES (1, "Dr Jones", "Chao", "+353895742514"),
        (2, "Dr Ryan", "Chao", "+353895742514"),
        (3, "Dr Smith", "Chao", "+353895742514");

INSERT INTO [procedure]
VALUES ("Physical exam", 300),
        ("X-Ray", 600),
        ("Blood Test", 100);

INSERT INTO apointment
VALUES (1, 1, 1, "15-09-2021", "Physical exam"),
        (2, 2, 2, "15-09-2021", "X-Ray"),
        (3, 3, 3, "15-09-2021", "Blood Test");