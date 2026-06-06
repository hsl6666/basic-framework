CREATE TABLE IF NOT EXISTS chat_turns (
    id BIGSERIAL PRIMARY KEY,
    session_id VARCHAR(128) NOT NULL,
    message TEXT NOT NULL,
    answer TEXT NOT NULL,
    engine VARCHAR(64) NOT NULL,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_chat_turns_session_id_created_at
    ON chat_turns (session_id, created_at DESC);

