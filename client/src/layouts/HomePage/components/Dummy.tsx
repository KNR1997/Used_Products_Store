import React, { useEffect, useState } from 'react'

const Dummy = () => {

    let [books, setBooks] = useState([])

    useEffect(() => {
        getBooks()
    }, [])

    let getBooks = async () => {
        let response = await fetch('http://localhost:8000/api/books')
        let data = await response.json()
        console.log(data)
        setBooks(data)
    }

  return (
    <div>Dummy</div>
  )
}

export default Dummy