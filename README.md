Rocket
======

About
-----
Rocket is a revolutionary new programming language oriented towards learning algorithms.

Syntax
------

Comments
	
	# Comment

Input and Output
	
	1;  # Statements containing single expressions are printed
	    # Outputs `1`
	
Literals
	
	1; 1.00;    # Number
	[1, 2.00];  # List

Variables and Operations

	number: 1.00;     # Set number or list to expression
	                  # `number` is now `1`
	number;           # Get number or list
	                  # Outputs `1`
	                  
	list: [1, 2.00];
	list@1:3;         # Set list element at index b to expression
	                  # `list` is now `[1, 3]`
	list@1;           # Get list element at index b
	                  # Outputs `3`

Number Operations

	+  # Add
	-  # Subtract
	*  # Multiply
	/  # Divide
	%  # Modulus
	^  # Power

List Operations

	$  # Length

Comparisons

	=  # Equal 
	>  # Greater
	<  # Less

Boolean

	&  # And
	|  # Or
	~  # Not

Grouping

	(<Expression>)  # Higher precedence operation

Control

	?(<expression>){}    # If
	?(<expression>){}{}  # If else
	!(<expression>){}    # While