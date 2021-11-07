
<b> Testing the blockchain: </b><br>
python3 -m backend.scripts.average_block_rate


**Activate the virtual environment**:
```source blockchain-env/bin/activate```


````python3 -m venv blockchain-env```` </br>
````python3 -m backend.blockchain.block```` </br>


**Run the tests**</br>
Make sure to activate the virtual env </br>
In Python version, type: </br>
```python3 -m pytest backend/tests```

</br>
Thank you David Katz for the source code regarding the Python version.


**Proof of work**</br>
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
How is the <b>proof of work system implemented here</b>?



**Chain validation**</br>

<ul>
    <li> Correct block fields present
    <li> Actual last_hash reference
    <li> Valid Hash
    <li> Valid Proof of Work
</ul>
