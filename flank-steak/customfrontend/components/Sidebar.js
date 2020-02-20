import React from 'react'
import List from '@material-ui/core/List'
import ListItem from '@material-ui/core/ListItem'
import ListItemText from '@material-ui/core/ListItemText'
import ListItemLink from '@material-ui/core/ListItem'
import Button from '@material-ui/core/Button'

function Sidebar() {
    return(
        <div className="sidebar">
            <List disablePadding dense>
                <ListItem button className="sidebarButton">
                    <Button href="/">Home</Button>
                    
                </ListItem>
                <ListItem button>
                    <Button href="/about">About</Button>
                </ListItem>
            </List>
        </div>
    )
}

export default Sidebar