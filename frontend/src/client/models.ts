export type Body_login_login_access_token = {
	grant_type?: string | null;
	username: string;
	password: string;
	scope?: string;
	client_id?: string | null;
	client_secret?: string | null;
};



export type HTTPValidationError = {
	detail?: Array<ValidationError>;
};



export type ItemCreate = {
	title: string;
	description?: string | null;
};



export type ItemPublic = {
	title: string;
	description?: string | null;
	id: number;
	owner_id: number;
};



export type ItemUpdate = {
	title?: string | null;
	description?: string | null;
};



export type ItemsPublic = {
	data: Array<ItemPublic>;
	count: number;
};



export type Message = {
	message: string;
};



export type NewPassword = {
	token: string;
	new_password: string;
};



export type Token = {
	access_token: string;
	token_type?: string;
};



export type UpdatePassword = {
	current_password: string;
	new_password: string;
};



export type UserCreate = {
	email: string;
	is_active?: boolean;
	is_superuser?: boolean;
	full_name?: string | null;
	password: string;
};



export type UserPublic = {
	email: string;
	is_active?: boolean;
	is_superuser?: boolean;
	full_name?: string | null;
	id: number;
};



export type UserRegister = {
	email: string;
	password: string;
	full_name?: string | null;
};



export type UserUpdate = {
	email?: string | null;
	is_active?: boolean;
	is_superuser?: boolean;
	full_name?: string | null;
	password?: string | null;
};



export type UserUpdateMe = {
	full_name?: string | null;
	email?: string | null;
};



export type UsersPublic = {
	data: Array<UserPublic>;
	count: number;
};



export type ValidationError = {
	loc: Array<string | number>;
	msg: string;
	type: string;
};

export type ZuPublic = {

	gid: number;
	cadastra2: string;
	address: string;
	hasvalid5: string;
	hascadas6: string;
	isdraft: string;
	ownershi8: string;
	is_stroy: string;
	area: string;
	geom: string;
	is_nonca20: string;

};

export type ZusPublic = {
	items: Array<ZuPublic>,
	page: number,
	has_more: boolean,
}

export type ZusDetails = {
	zu: ZuPublic,
}


import { Decimal } from 'decimal.js';
import { Geometry } from 'geojson';

export interface Okrug {
  gid?: number;
  name?: string;
  label?: string;
  shape_area: Decimal;
  geom: Geometry;
}

export interface Zu {
  gid?: number;
  cadastra2?: string;
  address?: string;
  hasvalid5?: string;
  hascadas6?: string;
  isdraft?: string;
  ownershi8?: string;
  is_stroy?: string;
  area: Decimal;
  geom: Geometry;
  comments: Comment[];
  is_nonca20: Decimal;
}

export interface Mkd {
  gid?: number;
  address?: string;
  cadastra3?: string;
  shape_area: Decimal;
  geom: Geometry;
}

export interface Oozt {
  gid?: number;
  status?: string;
  zoneid?: string;
  docnum?: string;
  docdate?: string;
  doclist?: string;
  geom: Geometry;
}

export interface PpGaz {
  gid?: number;
  reg_num?: string;
  vid_ppt?: string;
  name?: string;
  vid_doc_ra?: string;
  num_doc_ra?: string;
  data_doc_r?: string;
  zakazchik?: string;
  ispolnitel?: string;
  istoch_fin?: string;
  otvetst_mk?: string;
  num_kontra?: string;
  data_kontr?: string;
  vid_doc_ut?: string;
  num_doc_ut?: string;
  data_doc_u?: string;
  priostanov?: string;
  zaversheni?: string;
  otmena?: string;
  status?: string;
  grup1?: string;
  grup2?: string;
  oasi?: string;
  us_ppt?: string;
  shape_area: Decimal;
  geom: Geometry;
}

export interface PpMetroAll {
  gid?: number;
  reg_num?: string;
  vid_ppt?: string;
  name?: string;
  vid_doc_ra?: string;
  num_doc_ra?: string;
  data_doc_r?: string;
  zakazchik?: string;
  ispolnitel?: string;
  istoch_fin?: string;
  otvetst_mk?: string;
  num_kontra?: string;
  data_kontr?: string;
  vid_doc_ut?: string;
  num_doc_ut?: string;
  data_doc_u?: string;
  priostanov?: string;
  zaversheni?: string;
  otmena?: string;
  status?: string;
  grup1?: string;
  grup2?: string;
  oasi?: string;
  us_ppt?: string;
  shape_area: Decimal;
  geom: Geometry;
}

export interface PptAll {
  gid?: number;
  reg_num?: string;
  vid_ppt?: string;
  name?: string;
  vid_doc_ra?: string;
  num_doc_ra?: string;
  data_doc_r?: string;
  zakazchik?: string;
  ispolnitel?: string;
  istoch_fin?: string;
  otvetst_mk?: string;
  num_kontra?: string;
  data_kontr?: string;
  vid_doc_ut?: string;
  num_doc_ut?: string;
  data_doc_u?: string;
  priostanov?: string;
  zaversheni?: string;
  otmena?: string;
  status?: string;
  grup1?: string;
  grup2?: string;
  oasi?: string;
  us_ppt?: string;
  shape_area: Decimal;
  geom: Geometry;
}

export interface PptUds {
  gid?: number;
  reg_num?: string;
  vid_ppt?: string;
  name?: string;
  vid_doc_ra?: string;
  num_doc_ra?: string;
  data_doc_r?: string;
  zakazchik?: string;
  ispolnitel?: string;
  istoch_fin?: string;
  otvetst_mk?: string;
  num_kontra?: string;
  data_kontr?: string;
  vid_doc_ut?: string;
  num_doc_ut?: string;
  data_doc_u?: string;
  priostanov?: string;
  zaversheni?: string;
  otmena?: string;
  status?: string;
  grup1?: string;
  grup2?: string;
  oasi?: string;
  us_ppt?: string;
  shape_area: Decimal;
  geom: Geometry;
}

export interface Rayon {
  gid?: number;
  name?: string;
  shape_area: Decimal;
  shape_len: Decimal;
  geom: Geometry;
}

export interface Rsp {
  gid?: number;
  okrug?: string;
  rayon?: string;
  address?: string;
  area?: string;
  prim?: string;
  plotnost?: string;
  vysota?: string;
  spp?: string;
  total_area?: string;
  flat_area?: string;
  osnovanie?: string;
  arg?: string;
  objectid?: string;
  geom: Geometry;
}

export interface SpritZones {
  gid?: number;
  linecode?: string;
  name?: string;
  doc?: string;
  comment?: string;
  area: Decimal;
  geom: Geometry;
}

export interface Oks {
  gid?: number;
  address: string;
  cadastra3: string;
  shape_area: Decimal;
  geom: Geometry;
}

export interface TpzNew {
  gid?: number;
  podzone_nu?: string;
  num_pp?: string;
  doc_date?: Date;
  type?: string;
  plotnost?: string;
  vysota?: string;
  proczastro?: string;
  area?: Decimal;
  geom: Geometry;
}

export interface TzNew {
  gid?: number;
  zone_num: string;
  num_pp: string;
  doc_date: Date;
  type?: string;
  index_?: string;
  area: Decimal;
  geom: Geometry;
}

export interface UchastrkiMegevania {
  gid?: number;
  numberarea: number;
  dscr: string;
  klass?: string;
  func_use?: string;
  n_kvar?: string;
  n_park?: string;
  year?: string;
  area: Decimal;
  geom: Geometry;
}

export interface UdsBridges {
  gid?: number;
  vid?: string;
  name?: string;
  shape_leng: Decimal;
  shape_area: Decimal;
  geom: Geometry;
}

export interface UdsRoads {
  gid?: number;
  name_str?: string;
  vid_road?: string;
  ext_name?: string;
  shape_leng: Decimal;
  shape_area: Decimal;
  geom: Geometry;
}

export interface Zouit {
  gid?: number;
  cad_num?: string;
  okrug?: string;
  rayon_pos?: string;
  vid_zouit?: string;
  type_zone?: string;
  name?: string;
  organ?: string;
  doc?: string;
  shape_leng: Decimal;
  shape_area: Decimal;
  geom: Geometry;
}

export interface Krt {
  gid?: number;
  name?: string;
  type_krt?: string;
  area_krt: Decimal;
  geom: Geometry;
}

export interface ZuDetails {
  zu: ZuPublic;
  okrug: Okrug[];
  mkd: Mkd[];
  zouit: Zouit[];
  oozt: Oozt[];
  rayon: Rayon[];
  oks: Oks[];
  sprit: SpritZones[];
  krt: Krt[];
  pzz_tz: TzNew[];
  pzz_tpz: TpzNew[];
  rsp: Rsp[];
  bidges: UdsBridges[];
  roads: UdsRoads[];
}