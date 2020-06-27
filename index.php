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

    function fry($req) {
		// On each new POST request, we extract the transaction data
		$new_fry = json_encode($req->get('POST'));

		// Then we add the transaction to our list
		array_push($this->nodes_transactions, $new_fry);

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
}

/*
 *	ROUTING
 */
$f3->route('POST /fry', 
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