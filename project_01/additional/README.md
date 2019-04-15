## Additional task: Gradient descent using

# Results

* Original model (ADAM optimizer:  first-order gradient-based optimization )
   * Training 
        *acc: 0.9477  loss: 0.1450
   * Testing 
        *acc: 0.8804 Test loss: 0.3513
* SGD model (Stocahastic gradient desscent)
    * Training 
        *acc: 0.8183  loss: 0.4986
   * Testing 
        *acc: 0.8227 Test loss: 0.4885
    
 Brief (simple) reasoning: SGD has much slower convergence than Adam and therfor under all other similar coniditions
                           did not reach the same loss minimum and achieve the same level of accuracy as the ADAM model.
