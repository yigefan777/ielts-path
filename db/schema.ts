import { sqliteTable, text } from 'drizzle-orm/sqlite-core';
export const profiles = sqliteTable('profiles', { userId: text('user_id').primaryKey(), data: text('data').notNull(), updated: text('updated').notNull() });
export const records = sqliteTable('records', { id: text('id').primaryKey(), userId: text('user_id').notNull(), data: text('data').notNull(), updated: text('updated').notNull() });
export const vocabularyProgress = sqliteTable('vocabulary_progress', { id:text('id').primaryKey(), userId:text('user_id').notNull(), wordId:text('word_id').notNull(), status:text('status').notNull(), updated:text('updated').notNull() });
