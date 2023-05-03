
SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';
SET default_table_access_method = heap;

CREATE SCHEMA vam;

DROP TABLE vam.orders CASCADE;
DROP TABLE vam.transactions CASCADE;
DROP TABLE vam.users CASCADE;
DROP TABLE vam.artworks CASCADE;

CREATE TABLE vam.orders (
    order_id integer NOT NULL,
    user_id integer NOT NULL,
    artwork_id integer NOT NULL,
    price double precision NOT NULL,
    direction BOOLEAN NOT NULL DEFAULT FALSE,
    is_canceled BOOLEAN NOT NULL DEFAULT FALSE
);

-- NOTE: transactions doesn't need artwork id, artwork is tied to order id
-- NOTE: price can be different then order price
CREATE TABLE vam.transactions (
    transaction_id integer NOT NULL,
    price double precision NOT NULL,
    buy_order_id integer NOT NULL,
    sell_order_id integer NOT NULL
);

CREATE TABLE vam.users (
    user_id integer NOT NULL,
    firstname character varying(45) NOT NULL,
    lastname character varying(45) NOT NULL
);

CREATE TABLE vam.artworks (
    artwork_id integer NOT NULL,
    description_id character varying(45) NOT NULL
);

ALTER TABLE vam.orders OWNER TO postgres;
ALTER TABLE vam.transactions OWNER TO postgres;
ALTER TABLE vam.users OWNER TO postgres;
ALTER TABLE vam.artworks OWNER TO postgres;

ALTER TABLE ONLY vam.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (order_id);

ALTER TABLE ONLY vam.transactions
    ADD CONSTRAINT transactions_pkey PRIMARY KEY (transaction_id);

ALTER TABLE ONLY vam.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);

ALTER TABLE ONLY vam.artworks
    ADD CONSTRAINT artworks_pkey PRIMARY KEY (artwork_id);

ALTER TABLE ONLY vam.orders
    ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES vam.users(user_id);

ALTER TABLE ONLY vam.orders
    ADD CONSTRAINT fk_artwork_id FOREIGN KEY (artwork_id) REFERENCES vam.artworks(artwork_id);

ALTER TABLE ONLY vam.transactions
    ADD CONSTRAINT fk_buy_order_id FOREIGN KEY (buy_order_id) REFERENCES vam.orders(order_id);

ALTER TABLE ONLY vam.transactions
    ADD CONSTRAINT fk_sell_order_id FOREIGN KEY (sell_order_id) REFERENCES vam.orders(order_id);
    
    


