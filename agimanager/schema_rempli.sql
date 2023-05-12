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
DROP TABLE IF EXISTS "Commande_Agigreen";
CREATE TABLE IF NOT EXISTS "Commande_Agigreen" (
	"id"	INTEGER NOT NULL UNIQUE,
	"status"	TEXT DEFAULT 'En traitement',
	"h_achat"	INTEGER,
	"h_recep"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "Stock_Agilog";
CREATE TABLE IF NOT EXISTS "Stock_Agilog" (
	"id"	INTEGER NOT NULL UNIQUE,
	"quantite"	INTEGER NOT NULL,
	"id_piece"	INTEGER,
	FOREIGN KEY("id_piece") REFERENCES "Pieces"("id"),
	PRIMARY KEY("id")
);
DROP TABLE IF EXISTS "Pieces";
CREATE TABLE IF NOT EXISTS "Pieces" (
	"id"	INTEGER NOT NULL UNIQUE,
	"ref"	TEXT NOT NULL,
	"nom"	TEXT NOT NULL,
	"seuil_commande"	INTEGER,
	"seuil_recompletion"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "Kits" ("id","nom") VALUES (1,'Kit 1');
INSERT INTO "Kits" ("id","nom") VALUES (2,'Kit 2');
INSERT INTO "Kits" ("id","nom") VALUES (3,'Kit 3');
INSERT INTO "Kits" ("id","nom") VALUES (4,'Kit 4');
INSERT INTO "Kits" ("id","nom") VALUES (5,'Kit 5');
INSERT INTO "Kits" ("id","nom") VALUES (6,'Kit 6');
INSERT INTO "Kits" ("id","nom") VALUES (7,'Kit 7');
INSERT INTO "Kits" ("id","nom") VALUES (8,'Kit 8');
INSERT INTO "Kits" ("id","nom") VALUES (9,'Kit 9');
INSERT INTO "Kits" ("id","nom") VALUES (10,'Kit 10');
INSERT INTO "Kits" ("id","nom") VALUES (11,'Kit 11');
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (1,11,2);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (1,9,2);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (1,7,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (1,3,2);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (1,2,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (1,32,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (1,10,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (1,6,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (1,5,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (1,4,2);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (1,8,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (2,12,2);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (2,3,2);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (2,2,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (2,13,2);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (2,10,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (2,6,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (2,16,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (2,4,2);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (3,12,2);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (3,3,2);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (3,2,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (3,13,4);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (3,10,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (3,15,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (3,6,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (3,14,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (3,4,2);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (4,17,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (4,22,2);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (4,20,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (4,19,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (5,21,4);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (5,17,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (5,10,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (5,22,2);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (5,14,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (5,20,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (5,19,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (6,21,4);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (6,17,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (6,10,3);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (6,14,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (6,20,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (6,19,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (7,25,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (7,24,2);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (7,10,2);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (7,22,2);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (8,28,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (6,18,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (5,18,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (4,18,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (4,23,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (3,1,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (2,1,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (1,1,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (8,27,2);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (8,25,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (8,24,2);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (8,10,2);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (8,22,2);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (8,26,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (9,29,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (10,30,1);
INSERT INTO "Composition_Kit" ("id_Kit","id_piece","quantitee") VALUES (11,31,2);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (1,'B2*2','Brique 2*2','','');
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (2,'MY','Moyeu',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (3,'JT','Jante',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (4,'PN','Pneu',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (5,'PL2*2','Plaque lisse 2*2',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (6,'P2*4','Plaque 2*4',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (7,'GR','Grille',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (8,'RA','Renvoi d''angle',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (9,'FV','Feu Avant',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (10,'P1*4','Plaque 1*4',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (11,'FR','Feu Arriere',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (12,'GB','Garde Boue',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (13,'P1*3','Plaque 1*3',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (14,'P4*4','Plaque 4*4',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (15,'P2*12','Plaque 2*12',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (16,'P2*8','Plaque 2*8',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (17,'PB','Pare-Brise',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (18,'AT','Attache',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (19,'VL','Volant',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (20,'SG','Siege',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (21,'FN','Fenetre',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (22,'P1*6','Plaque 1*6',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (23,'AC','Arceau',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (24,'P1*1','Plaque 1*1',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (25,'EQ','Equerre',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (26,'TT','Toit',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (27,'B2*4','Brique 2*4',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (28,'B1*4','Brique 1*4',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (29,'An','Antenne',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (30,'CA','Crochet d''attelage',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (31,'AA','Attache Accessoire',NULL,NULL);
INSERT INTO "Pieces" ("id","ref","nom","seuil_commande","seuil_recompletion") VALUES (32,'P1*2','Plaque 1*2',NULL,NULL);
COMMIT;
