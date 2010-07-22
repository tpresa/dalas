--
-- PostgreSQL database dump
--

SET client_encoding = 'LATIN1';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

--
-- Name: postla; Type: SCHEMA; Schema: -; Owner: loguser
--

CREATE SCHEMA postla;


ALTER SCHEMA postla OWNER TO loguser;

SET search_path = postla, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: genericlog; Type: TABLE; Schema: postla; Owner: loguser; Tablespace: 
--

CREATE TABLE genericlog (
    id bigint,
    data character varying(1000)
);


ALTER TABLE postla.genericlog OWNER TO loguser;

--
-- Name: rawlog; Type: TABLE; Schema: postla; Owner: loguser; Tablespace: 
--

CREATE TABLE rawlog (
    id integer NOT NULL,
    data character varying(1000)
);


ALTER TABLE postla.rawlog OWNER TO loguser;

--
-- Name: rawlog_id_seq; Type: SEQUENCE; Schema: postla; Owner: loguser
--

CREATE SEQUENCE rawlog_id_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE postla.rawlog_id_seq OWNER TO loguser;

--
-- Name: rawlog_id_seq; Type: SEQUENCE OWNED BY; Schema: postla; Owner: loguser
--

ALTER SEQUENCE rawlog_id_seq OWNED BY rawlog.id;


--
-- Name: id; Type: DEFAULT; Schema: postla; Owner: loguser
--

ALTER TABLE rawlog ALTER COLUMN id SET DEFAULT nextval('rawlog_id_seq'::regclass);

--
-- PostgreSQL database dump complete
--

