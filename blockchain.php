<?php

/**
 * This is the blockchain structure for the fun crypto BunDauCoin
 * ***
 * It's hightly inspired by this article:
 * > https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b 
 */

/*
 * Defining the structure of a BunDauBlock
 */
class BDBlock {
	public int $index;
	public int $timestamp;
	public string $data;
	public string $previous_hash;
	public string $hash;

	function __construct($index, $timestamp, $data, $previous_hash) {
		$this->index = $index;
		$this->timestamp = $timestamp;
		$this->data = $data;
		$this->previous_hash = $previous_hash;
		$this->hash = hash('sha256', $this);
	}

	function __toString(){
		return "BunDauBlock #{$this->index}";
	}

	function hash_block(){
		// Hashed with the sha256 algorithm
		// Makes sure it's encode in utf-8
		// returns the combined hash value in Hexadecimals
		return hash('sha256', utf8_encode("{$this->index}{$this->timestamp}{$this->data}{$this->previous_hash}"));
	}
}

function make_genesis_block() {
	// Makes the first block in the BDC blockchain.
	return new BDBlock(0, intval(date(time())), "Genesis Block", 0);
}

// Creating all the later BunDauBlocks in the BunDauCoin blockchain
function next_block(BDBlock $last_block, string $data = ""){
	$idx = $last_block->index + 1;

	// Create new BDBlock
	return new BDBlock($idx, intval(date(time())), "{$data}{$idx}", $last_block->hash);
}


/*
	Tests
 */
function testBlockChain() {
	// Create the first block
	$blockchain = array();
	array_push($blockchain, make_genesis_block());

	echo "INIT the BunDauBlock (BDC) with {$blockchain[0]}\n";
	echo "Hash: {$blockchain[0]->hash}\n\n";

	// Init previous ref
	$prev_block = $blockchain[0];

	// Generate some coins
	// (POC)
	for ($i=0; $i < 20; $i++) { 
		$block = next_block($prev_block, "I <3 Bun Dau Coin ! {$i}");
		array_push($blockchain, $block);
		$prev_block = $block;

		echo "{$block} added to blockchain.\n";
		echo "Hash: {$block->hash}\n\n";
	}
}