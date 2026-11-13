export type SceneData = {
  id: string;
  title: string;
  text: string;
  durationInFrames: number;
  background: string;
  image: string; // path relative to public/, or ""
  audio: string; // path relative to public/, or ""
};

export type VideoData = {
  fps: number;
  width: number;
  height: number;
  scenes: SceneData[];
};

export type VideoProps = {data: VideoData};
