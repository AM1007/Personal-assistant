# Personal-assistant

## Commands

The application supports the following commands:

- add [Name]: Створення нового запису контакту з указаним іменем.
- edit [Contact_id] [new_Name]: Редагування назви запису контакту.
- del [Contact_id]: Видалення запису контакту
- add-phone [Contact_id] [Phone]: Додання телефонного номеру контакту
- edit-phone [Contact_id] [Phone] [new_Phone]: Заміна телефонного контакту
- del-phone [Contact_id] [Phone]: Видалення номера телефону з контакту
- add-email [Contact_id] [Email]: Додання адреси електронної пошти до контакту.
- edit-email [Contact_id] [Email] [new_Email]: Replace an email address in a contact.
- del-email [Contact_id] [Email]: Заміна адреси електронної пошти в контакті.
- birthday [Contact_id] [Birthday]: Встановлення дня народження для контакту.
- del-birthday [Contact_id]: Видалення дня народження для контакту.
- address [Contact_id] [Address]: Додання адреси до контакту.
- del-address [Contact_id]: Видалення адреси від контакту.
- find [searchstring]: Пошук записів контактів на основі пошукового рядка
- help: Відображення списку доступних команд.
- note: Додання нотатки до блокнота
- all-notes: Список усіх приміток
- edit-note [Note_id] [Note]: Редагування тексту примітки
- del-note [Note_id]: Видалення нотатки із записника
- add-tag [Note_id] [Tag]: Додання тег до нотатки
- del-tag [Note_id] [Tag]: Видалення тегу від нотатки
- find-notes [searchstring]: Список всіх нотаток із даними рядка пошуку в нотатках і тегах. Пошуковий рядок має містити мінімум 2 символи
- find-tags [searchstring]: Перелік всіх нотатків з даними рядка пошуку в тегах. Рядок пошуку має містити мінімум 2 символи
- sort-tag: Список усіх нотаток, упорядкованих за кількістю тегів
- next-birthdays [int]: Відображення майбутніх днів народження протягом вказаної кількості днів.
- all: Перелік всіх записів контактів.
- close or exit: Виход з програми.
