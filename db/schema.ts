import { sqliteTable, text } from 'drizzle-orm/sqlite-core';
export const profiles = sqliteTable('profiles', { userId: text('user_id').primaryKey(), data: text('data').notNull(), updated: text('updated').notNull() });
export const records = sqliteTable('records', { id: text('id').primaryKey(), userId: text('user_id').notNull(), data: text('data').notNull(), updated: text('updated').notNull() });
