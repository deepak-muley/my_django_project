BEGIN;
CREATE TABLE "Country" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(50) NOT NULL,
    "url" varchar(200),
    "is_active" bool NOT NULL,
    "description" text,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
)
;
CREATE TABLE "CurrencyInfo" (
    "id" integer NOT NULL PRIMARY KEY,
    "country_id" integer NOT NULL REFERENCES "Country" ("id"),
    "code" varchar(3) NOT NULL,
    "symbol" varchar(3) NOT NULL,
    "unit" varchar(50) NOT NULL,
    "is_subunit" bool NOT NULL,
    "url" varchar(200),
    "is_active" bool NOT NULL,
    "description" text,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
)
;
CREATE TABLE "Mint" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(100) NOT NULL,
    "country_id" integer NOT NULL REFERENCES "Country" ("id"),
    "url" varchar(200),
    "is_active" bool NOT NULL,
    "description" text,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
)
;
CREATE TABLE "Bank" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(100) NOT NULL,
    "country_id" integer NOT NULL REFERENCES "Country" ("id"),
    "url" varchar(200),
    "is_active" bool NOT NULL,
    "description" text,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
)
;
CREATE TABLE "BankNote" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    "bank_id" integer NOT NULL REFERENCES "Bank" ("id"),
    "mint_id" integer NOT NULL REFERENCES "Mint" ("id"),
    "unit_id" integer NOT NULL REFERENCES "CurrencyInfo" ("id"),
    "value" integer NOT NULL,
    "signed_by" varchar(50),
    "series" varchar(100),
    "serial_number" varchar(100),
    "material" varchar(10) NOT NULL,
    "obverse_img" varchar(100) NOT NULL,
    "obverse_desc" text,
    "reverse_img" varchar(100) NOT NULL,
    "reverse_desc" text,
    "grade" varchar(5) NOT NULL,
    "status" varchar(50) NOT NULL,
    "main_color" varchar(100),
    "issue_date" date NOT NULL,
    "dimensions" varchar(100),
    "url" varchar(200),
    "tags_input" varchar(255) NOT NULL,
    "is_active" bool NOT NULL,
    "description" text,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
)
;
CREATE INDEX "CurrencyInfo_534dd89" ON "CurrencyInfo" ("country_id");
CREATE INDEX "Mint_534dd89" ON "Mint" ("country_id");
CREATE INDEX "Bank_534dd89" ON "Bank" ("country_id");
CREATE INDEX "BankNote_403f60f" ON "BankNote" ("user_id");
CREATE INDEX "BankNote_1862eb86" ON "BankNote" ("bank_id");
CREATE INDEX "BankNote_70541b58" ON "BankNote" ("mint_id");
CREATE INDEX "BankNote_cac2c6" ON "BankNote" ("unit_id");
COMMIT;
