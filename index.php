<?php 

require 'vendor/autoload.php';
require_once('blockchain.php');

/*
 *	INIT
 */
$f3 = \Base::instance();
$logger = new \Log("error.log");

/*
 *	Crypto-Transaction
 *	aka the Fry Pan !
 */

class FryPan {

	// Store the transactions that this node has in a list
	protected Array $nodes_transactions = array();

	public function dip($req) {
		// On each new POST request, we extract the transaction data
		$new_fry = json_encode($req->get('POST'));

		// Then we add the transaction to our list
		$this->nodes_transactions[] = $new_fry;

		// Because the transaction was successfully submitted, we log it to our console
		$new_fry = json_decode($new_fry);

		$GLOBALS['logger']->write( 
			"[New transaction] "
			. "FROM: {$new_fry->from} - "
			. "TO: {$new_fry->to} - "
			. "AMOUNT: {$new_fry->amount}" );
		
		# Then we let the client know it worked out
		return "Transaction submission successful";
	}

	private function proof_of_work(int $last_proof){
		// Create a variable that we will use to find our next proof of work
		$incrementor = $last_proof + 1;
  
		// Keep incrementing the incrementor until it's equal to a number divisible 
		// by 9 and the proof of work of the previous block in the chain
		while ($incrementor % 14 != 0 && $incrementor % $last_proof != 0) {
			$incrementor ++;
		}

		// Once that number is found, we can return it as a proof of our work
		return $incrementor;
	}

	public function fry(){
	  // Get the last proof of work
	  $last_block = $GLOBALS['blockchain'][ sizeof($GLOBALS['blockchain']) - 1];
	  $last_proof = $last_block->data['proof-of-work'];

	  // Find the proof of work for the current block being mined
	  // Note: The program will hang here until a new proof of work is found
	  $proof = $this->proof_of_work($last_proof);
	  
	  // Once we find a valid proof of work, we know we can mine a block so we reward the miner by adding a transaction
	  array_push($this->nodes_transactions, 
	  	json_encode( array(
	  		"from" => "network", 
	  		"to" => $miner_address, 
	  		"amount" => 1) )
	  );

	  // Now we can gather the data needed to create the new block
	  $newBDB_data = [
		"proof-of-work" => $proof,
		"transactions" => $this->nodes_transactions
	  ];
	  $newBDB_index = $last_block->index + 1;
	  $newBDB_timestamp = intval(date(time()));
	  $last_block_hash = hash('sha256', $last_block);

	  // Empty transaction list
	  $this->nodes_transactions = array();
	  // Now create the  new block!
	  $minedBDB = new BDBlock (
		$newBDB_index,
		$newBDB_timestamp,
		$newBDB_data,
		$last_block_hash
	  );
	  
	  array_push($GLOBALS['blockchain'], $minedBDB);
	  
	  # Let the client know we mined a block
	  return json_encode(array(
		  "index" => $new_block_index,
		  "timestamp" => $new_block_timestamp,
		  "data" => $new_block_data,
		  "hash" => $last_block_hash
	  )) . "\n";
	
	}
}

/*
 *	ROUTING
 */
$f3->route('POST /dip', 
	/*
		Request should looks like this : 
		$ curl \
		--data "from=random-public-key-a&to=random-public-key-b&amount=3" \
		-X POST http://localhost:8000/dip
	 */
	"FryPan->dip");

$f3->route('GET /fry', 
	/*
		Request should looks like this : 
		$ curl \
		--data "from=random-public-key-a&to=random-public-key-b&amount=3" \
		-X POST http://localhost:8000/fry
	 */
	"FryPan->fry");

/*
 *	RUN
 */
$f3->run();