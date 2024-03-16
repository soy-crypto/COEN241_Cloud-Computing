from mininet.topo import Topo

class BinaryTreeTopo( Topo ):
    "Binary Tree Topology Class."

    def __init__( self ):
        "Create the binary tree topology."

        # Initialize topology
        Topo.__init__( self )

	# Add hosts
	Host1 = self.addHost( 'h1' )
	Host1 = self.addHost( 'h2' )
	Host1 = self.addHost( 'h3' )
	Host1 = self.addHost( 'h4' )
	Host1 = self.addHost( 'h5' )
	Host1 = self.addHost( 'h6' )
	Host1 = self.addHost( 'h7' )
	Host1 = self.addHost( 'h8' )

	# Add switches
	Switch1 = self.addSwitch('s1')
	Switch1 = self.addSwitch('s2')
	Switch1 = self.addSwitch('s3')
	Switch1 = self.addSwitch('s4')
	Switch1 = self.addSwitch('s5')
	Switch1 = self.addSwitch('s6')
	Switch1 = self.addSwitch('s7')
	  
	# Add links
	self.addLink( Host1, Switch3 )
        self.addLink( Host2, Switch3 )
        self.addLink( Host3, Switch4 )
        self.addLink( Host4, Switch4 )
        self.addLink( Host5, Switch6 )
        self.addLink( Host6, Switch6 )
        self.addLink( Host7, Switch7 )
        self.addLink( Host8, Switch7 )
        
        
        self.addLink( Switch2, Switch3 )
        self.addLink( Switch2, Switch4 )
        self.addLink( Switch5, Switch6 )
        self.addLink( Switch5, Switch7 )
        self.addLink( Switch1, Switch2 )
        self.addLink( Switch1, Switch5 )

topos = { 'binary_tree': ( lambda: BinaryTreeTopo() ) }
