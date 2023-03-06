import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Like(props) {
  const [liked, setLiked] = useState(false);
  const [likeCount, setLikeCount] = useState(0);

  useEffect(() => {
    // fetch the initial like count and whether the user has liked the post when the component mounts
    
    axios.get(`http://localhost:8000/api/posts/${props.postId}/like/`)
      .then(response => {
        setLikeCount(response.data.count);
        setLiked(response.data.liked);
      })
      .catch(error => console.log(error));
  }, [props.postId]);

  const handleLike = () => {
    const increment = liked ? -1 : 1;
    setLikeCount(likeCount + increment);
    setLiked(!liked);

    if (liked) {
      axios.delete(`http://localhost:8000/api/posts/${props.postId}/like/`)
        .then(response => console.log(response))
        .catch(error => console.log(error));
    } else {
      axios.post(`http://localhost:8000/api/posts/${props.postId}/like/`)
        .then(response => console.log(response))
        .catch(error => console.log(error));
    }
  }

  return (
    <div>
      <button onClick={handleLike}>{liked ? 'Unlike' : 'Like'}</button>
      <p>{likeCount} likes</p>
    </div>
  );
}

export default Like;
