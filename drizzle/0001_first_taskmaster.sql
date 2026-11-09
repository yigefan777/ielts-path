CREATE TABLE `vocabulary_progress` (
	`id` text PRIMARY KEY NOT NULL,
	`user_id` text NOT NULL,
	`word_id` text NOT NULL,
	`status` text NOT NULL,
	`updated` text NOT NULL
);
