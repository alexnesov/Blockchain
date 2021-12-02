
<b> Testing the blockchain: </b><br>

```
python3 -m backend.scripts.average_block_rate
```


**Activate the virtual environment**:
```
source blockchain-env/bin/activate
```


```
python3 -m venv blockchain-env
```

```
python3 -m backend.blockchain.block
```
</br>


**To run the tests:**</br>
Make sure to activate the virtual env </br>
```
python3 -m pytest backend/tests
```

<hr>

### Proof of work
Crucial for the stable work of the blockchain. </br>

<b>Proof of work</b> is a mechanism that requires miners to solve a computational puzzle in order to create valid
blocks. Solving the puzzle requires a brute-force algorithm that demands CPU power (hence, the analogy of mining the block)


Everyone can create a block.</br>
We need to implement methods that will actually validate the newly created blocks. We need to make sure that the received blocks are
formatted properly and follow the rules of our blockchain, such as:

<ul>
    <li> Having the proper number of leading 0's for the proof of work requirement.
    </br> It is the standard proof of work implementation for finding valid blocks. By adjusting a nonce value in the block, the miner has an infinite number of tries at generating new hashes.
    Once the miner finds a hash with a matching number of leading 0's as the block difficulty, the fields for a valid new block have been found. </li>
    <li> A valid hash </li>
</ul>


</br>



**Chain validation**</br>

<ul>
    <li> Correct block fields present
    <li> Actual last_hash reference
    <li> Valid Hash
    <li> Valid Proof of Work
</ul>

### Blockchain network

The idea is that each individual in the network will own a blockchain instance and they should be able to <b>interact</b> with it whenever they want.
So, to facilitate a system where an individual has their own blochchain instance we're gonna setup an API.

We're gonna start by implementing two main methods:

<ul>
<li> One reading the block and change data. That way you can figure out the contents of the blockchain data itself
<li> One to add and mine a new block
</ul>

How are we gonna interact with the API? We're going to set up a webserver.
The server is gonna expose a handful of HTTP requests.
We're gonna use <b>Flask</b> to set up this server.

</br>
</br>

**Run the application and API**

```
python3 -m backend.app
```


### Real-time messaging network through pub/sub

We need the ability to broadcast update of a local blockchain to all the peers of a network.
To implement this capbility we will take advantage of what we call the sub/pub (Subscriber/Publisher) pattern.


We'll create multiple channels:

    - The block channel 


We'll use PubNub to create this server to server communication layer


<b>Thank you David Katz for the source code regarding the Python version.</b>

