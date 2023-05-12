BEGIN TRANSACTION;
DROP TABLE IF EXISTS "Kits";
CREATE TABLE IF NOT EXISTS "Kits" (
	"id"	INTEGER NOT NULL UNIQUE,
	"nom"	TEXT UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "Composition_leanCmd_piece";
CREATE TABLE IF NOT EXISTS "Composition_leanCmd_piece" (
	"id_cmd"	INTEGER NOT NULL,
	"id_piece"	INTEGER NOT NULL,
	"quantite"	INTEGER,
	FOREIGN KEY("id_cmd") REFERENCES "Commande_Agilean"("id"),
	FOREIGN KEY("id_piece") REFERENCES "Pieces"("id")
);
DROP TABLE IF EXISTS "Composition_leanCmd_kit";
CREATE TABLE IF NOT EXISTS "Composition_leanCmd_kit" (
	"id_cmd"	INTEGER NOT NULL,
	"id_kit"	INTEGER NOT NULL,
	"quantite"	INTEGER NOT NULL,
	FOREIGN KEY("id_kit") REFERENCES "Kits"("id"),
	FOREIGN KEY("id_cmd") REFERENCES "Commande_Agilean"("id")
);
DROP TABLE IF EXISTS "Composition_Kit";
CREATE TABLE IF NOT EXISTS "Composition_Kit" (
	"id_Kit"	INTEGER NOT NULL,
	"id_piece"	NUMERIC NOT NULL,
	"quantitee"	INTEGER,
	FOREIGN KEY("id_Kit") REFERENCES "Kits"("id"),
	FOREIGN KEY("id_piece") REFERENCES "Pieces"("id")
);
DROP TABLE IF EXISTS "Pieces";
CREATE TABLE IF NOT EXISTS "Pieces" (
	"id"	INTEGER NOT NULL UNIQUE,
	"ref"	TEXT NOT NULL,
	"nom"	TEXT NOT NULL,
	"seuil_commande"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "Composition_greenCmd_piece";
CREATE TABLE IF NOT EXISTS "Composition_greenCmd_piece" (
	"id_cmd"	INTEGER,
	"id_piece"	NUMERIC,
	"quantite"	INTEGER,
	FOREIGN KEY("id_piece") REFERENCES "Pieces"("id"),
	FOREIGN KEY("id_cmd") REFERENCES "Commande_Agigreen"("id")
);
DROP TABLE IF EXISTS "timer";
CREATE TABLE IF NOT EXISTS "timer" (
	"id"	INTEGER NOT NULL UNIQUE,
	"start_timestamp"	INTEGER NOT NULL,
	"pause_elapsed_time"	INTEGER DEFAULT 0,
	"pause_timestamp"	INTEGER DEFAULT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "Commande_Agilean";
CREATE TABLE IF NOT EXISTS "Commande_Agilean" (
	"id"	INTEGER NOT NULL UNIQUE,
	"status"	INTEGER NOT NULL DEFAULT 'En attente',
	"h_achat"	TEXT,
	"h_production"	INTEGER,
	"h_envoi"	INTEGER,
	"h_recep"	INTEGER DEFAULT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "Stock_Agilog";
CREATE TABLE IF NOT EXISTS "Stock_Agilog" (
	"id"	INTEGER NOT NULL UNIQUE,
	"quantite"	INTEGER NOT NULL,
	"id_piece"	INTEGER,
	PRIMARY KEY("id")
);
DROP TABLE IF EXISTS "Commande_Agigreen";
CREATE TABLE IF NOT EXISTS "Commande_Agigreen" (
	"id"	INTEGER NOT NULL UNIQUE,
	"status"	TEXT DEFAULT 'En traitement',
	"h_achat"	INTEGER,
	"h_recep"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
COMMIT;
