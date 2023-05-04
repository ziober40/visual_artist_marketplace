
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

-- CREATE SCHEMA vam;

DROP TABLE public.orders CASCADE;
DROP TABLE public.transactions CASCADE;
DROP TABLE public.users CASCADE;
DROP TABLE public.artworks CASCADE;

CREATE TABLE public.orders (
    order_id SERIAL PRIMARY KEY,
    user_id integer NOT NULL,
    artwork_id integer NOT NULL,
    price double precision NOT NULL,
    direction BOOLEAN NOT NULL DEFAULT FALSE,
    is_canceled BOOLEAN NOT NULL DEFAULT FALSE,
    is_executed BOOLEAN NOT NULL DEFAULT FALSE
);

-- NOTE: transactions doesn't need artwork id, artwork is tied to order id
-- NOTE: price can be different then order price
CREATE TABLE public.transactions (
    transaction_id SERIAL PRIMARY KEY,
    price double precision NOT NULL,
    buy_order_id integer NOT NULL,
    sell_order_id integer NOT NULL
);

CREATE TABLE public.users (
    user_id SERIAL PRIMARY KEY,
    firstname character varying(45) NOT NULL,
    lastname character varying(45) NOT NULL
);

CREATE TABLE public.artworks (
    artwork_id SERIAL PRIMARY KEY,
    description_id character varying(45) NOT NULL
);

ALTER TABLE public.orders OWNER TO postgres;
ALTER TABLE public.transactions OWNER TO postgres;
ALTER TABLE public.users OWNER TO postgres;
ALTER TABLE public.artworks OWNER TO postgres;

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES public.users(user_id);

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT fk_artwork_id FOREIGN KEY (artwork_id) REFERENCES public.artworks(artwork_id);

ALTER TABLE ONLY public.transactions
    ADD CONSTRAINT fk_buy_order_id FOREIGN KEY (buy_order_id) REFERENCES public.orders(order_id);

ALTER TABLE ONLY public.transactions
    ADD CONSTRAINT fk_sell_order_id FOREIGN KEY (sell_order_id) REFERENCES public.orders(order_id);