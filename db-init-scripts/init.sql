-- Create table for gene variants
CREATE TABLE gene_variants (
    id SERIAL PRIMARY KEY,
    gene VARCHAR(50),
    type VARCHAR(50),
    alteration VARCHAR(50),
    alt_type VARCHAR(50)
);

-- Insert example data
INSERT INTO gene_variants (gene, type, alteration, alt_type) VALUES
('KRAS', 'Main', 'Q61H', 'MUT'),
('NRAS', 'Main', 'WT', 'WT'),
('APC', 'Main', 'T664fs*6', 'MUT'),
('CHEK2', 'Main', 'amplification', 'AMP'),
('BCL2L1', 'Main', 'amplification', 'AMP'),
('SRC', 'Main', 'amplification', 'AMP'),
('TP53', 'Main', 'R248W', 'MUT'),
('ARID1A', 'Main', 'Q1519*', 'MUT'),
('ASXL1', 'VUS', 'amplification', 'AMP'),
('BRCA2', 'VUS', 'amplification', 'AMP');