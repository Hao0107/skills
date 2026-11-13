import React from 'react';
import {Composition, staticFile} from 'remotion';
import {ScriptVideo} from './Video';
import type {VideoData, VideoProps} from './types';

const emptyData: VideoData = {fps: 30, width: 1920, height: 1080, scenes: []};

export const Root: React.FC = () => (
  <Composition
    id="ScriptVideo"
    component={ScriptVideo}
    durationInFrames={1}
    fps={30}
    width={1920}
    height={1080}
    defaultProps={{data: emptyData} satisfies VideoProps}
    // Load public/scenes.json and derive duration/size from it.
    calculateMetadata={async () => {
      const res = await fetch(staticFile('scenes.json'));
      const data = (await res.json()) as VideoData;
      return {
        durationInFrames: Math.max(
          1,
          data.scenes.reduce((sum, s) => sum + s.durationInFrames, 0),
        ),
        fps: data.fps,
        width: data.width,
        height: data.height,
        props: {data},
      };
    }}
  />
);
