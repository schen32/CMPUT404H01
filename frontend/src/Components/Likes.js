import React, { useState, useEffect } from "react";
import axios from "axios";

function Like({ postId, userId }) {
  const [liked, setLiked] = useState(false);
  const [likeCount, setLikeCount] = useState(0);

  useEffect(() => {
    // fetch the initial like count and whether the user has liked the post when the component mounts
    let path = 'http://localhost:8000/api/posts/' + postId +'/like/';
    axios
      .get(path)
      .then((response) => {
        setLikeCount(response.data.count);
        setLiked(response.data.liked);
      })
      .catch((error) => console.log(error));
  }, []);

  const handleLike = () => {
    let path = 'http://localhost:8000/api/posts/' + postId +'/like/';
    let data = {
      user: userId,
      post: postId,
    };
    axios
      .post(path, data)
      .then((response) => {
        setLiked(true);
        setLikeCount(response.data.count);
      })
      .catch((error) => console.log(error));
  };

  const handleUnlike = () => {
    let path = 'http://localhost:8000/api/posts/' + postId +'/like/';
    let data = {
      id: userId,
      post: postId,
    };
    axios
      .delete(path, { data })
      .then((response) => {
        setLiked(false);
        setLikeCount(response.data.count);
      })
      .catch((error) => console.log(error));
  };

  return (
    <div>
      <button onClick={liked ? handleUnlike : handleLike}>
        {liked ? "Unlike" : "Like"}
      </button>
      <span>{likeCount} likes</span>
    </div>
  );
}

export default Like;
